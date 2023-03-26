
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from config import bot, ADMINS


async def breast_and_biceps(bot: Bot):
    await bot.send_message(ADMINS[0], 'Сегодня качаем грудь и бицепс,удачной тренировки❤')

async def back_and_triceps(bot: Bot):
    await bot.send_message(ADMINS[0], 'Сегодня качаем спину и трицепс,удачной тренировки❤')

async def leg_and_shoulders(bot: Bot):
    await bot.send_message(ADMINS[0], 'Сегодня качаем ноги и плечи,удачной тренировки❤')

async def birthday(bot: Bot):
    await bot.send_message(ADMINS[0], 'С днем рождения хозяин❤')

async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    scheduler.add_job(
        breast_and_biceps,
        trigger=CronTrigger(
            day_of_week=1,
            hour=12,
            minute=0
        ),
        kwargs={"bot": bot},
    )

    scheduler.add_job(
        back_and_triceps,
        trigger=CronTrigger(
            day_of_week=3,
            hour=12,
            minute=0
        ),
        kwargs={"bot": bot},
    )

    scheduler.add_job(
        leg_and_shoulders,
        trigger=CronTrigger(
            day_of_week=5,
            hour=12,
            minute=0
        ),
        kwargs={"bot": bot},
    )

    scheduler.add_job(
        birthday,
        trigger=CronTrigger(
            month=6,
            day=20,
            hour=00,
            minute=0
        ),
        kwargs={"bot": bot},
    )
    scheduler.start()