from django.core.management.base import BaseCommand
from django.db.models import Avg
from app.log.models import MinuteLog, HourLog
from app.machine.models import Config


class Command(BaseCommand):
    def handle(self, *args, **options):

        machines = MinuteLog.objects.filter(sync=False).values('machine', 'machine__count').distinct()

        for item in machines:
            avg = MinuteLog.objects.filter(machine__id=item['machine']).aggregate(Avg('rate'))

            need_send = False
            config = Config.objects.get(count=item['machine__count'])

            # высчитываем процент отклонения
            perc = (avg * 100) / config.avg

            # проверяем отклонение с табличным
            if abs(100-perc) >= config.variance:
                need_send = True

            hour = HourLog(
                machine_id=item['machine'],
                rate=int(avg['rate__avg']),
                send=need_send
            )
            hour.save()
        self.stdout.write(self.style.SUCCESS('Successfully rotation logs'))
