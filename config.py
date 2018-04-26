import sys

module = sys.modules[__name__]

def setCell( name, value ):
	module.table[name] = value

def getCell( name ):
	return module.table.get( name )

def initConfig():
	module.table = {}


	#############################################################
	########                                             ########
	########           Основные настройки бота           ########
	########                                             ########
	#############################################################


	setCell( "vk_msgForPick", 1 ) # Сколько сообщений за раз обрабатывать? Просто не трогай...

	setCell( "vk_AddFriends", 0 ) # Автоматически добавлять новых пользователей в друзья?

	setCell( "vk_login", "+79106116852" ) # Логин от аккаунта ВК
	setCell( "vk_password", "scarlet" ) # Пароль от аккаунта ВК

	setCell( "telegram_token", "470919092:AAHUO4Uvk2MnTKHnJn-7FZ6dRmZjrd9KtdY" ) # Токен ботинка в Telegram


	#############################################################
	########                                             ########
	########      Настройки стикеров Telegram--> VK      ########
	########                                             ########
	#############################################################


	setCell( "vk_EnableStickers", 1 ) # Включить отправку стикеров из Telegram в ВК?

	setCell( "vk_album_id", 249367765 ) # ID альбома, куда будут заливаться стикеры из тележки
	setCell( "vk_detelestickers", 1) # Удалять загруженные стикеры с компьютера?
	# После загрузки в ВК они ни на что не влияют, так что при желании можно оставить
	# Они будут скапливаться в папке 'stickers'
	setCell( "vk_sticker_EnableScale", 1) # Включить уменьшение стикера в ВК?
	# Можно и не включать, но тогда стикер будет просто огромный
	setCell( "vk_sticker_size", 200 ) # Развер стикера в ВК.
	# Можно поэксперементировать с размерами, но 200 мне показался самым удачным
	# P.S. Не забываем про то, что размер у залитых ранее стикеров не изменится!


	#############################################################
	########                                             ########
	########     Настройка тоннелей ВК <--> Telegram     ########
	########                                             ########
	#############################################################



	setCell( "vk_30", '@group3stom' ) # Пример переадресации из чата ВК в Telegram

	# P.S. В нашем случае 1 - 'локальный' ID чата для аккаунта ВК

	setCell( "vk_31", '@starostyhuyarosty' ) # Пример переадресации ЛС ВК в Telegram

	setCell( "t_-236472090", '417110104' ) # Пример переадресации ЛС ВК в Telegram

	setCell( "vk_41", '@starostyhuyarosty' ) # Шаблон

	setCell( "t_-1", '111111' ) # Шаблон
   
