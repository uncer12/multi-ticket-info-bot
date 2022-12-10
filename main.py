import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
import env
from discord import ui


PREFIX = '/' # prefix commands для активации команды (не слэшь команд)
bot = commands.Bot(command_prefix= PREFIX, intents = discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot is ready!')
    try:
        synced = await bot.tree.sync()
        print(f'Synnced {len(synced)} command(s)')
    except Exception as e:
            print(e)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Majestic 5")) #Статус - онлайн, Активность дискорда - играет в....

@bot.event
async def on_member_join( member ):
    channel = bot.get_channel(1027576029486792725) #Вывод сообщений о приоединении человека в (channel_ID)
    role = discord.utils.get( member.guild.roles, id = 1027575987422121985 ) # Автоматическая выдача роли новым пользователям (roles_ID)
    await member.add_roles( role )
    ####
    # Вывод сообщения в личные сообщения новому пользователю.
    ####
    await channel.send( embed = discord.Embed (colour = discord.Color.red(), description = f'**Пользователь <@{member.id}>, присоединился к нам.**\nНачать общение в сообществе рекомендуем с ввода *slash command* `/start`.'))
    await member.send (f'<@{member.id}> **Привет!**\n*Сделайте Ваше имя по следующей форме:* `Принадлежность | Nick_Name | Static ID`')
    await member.send ('> Для продолжения работы просим ознакомиться с командами, используй *slash command* `/help`\n> И помни, что **любое** нарушение правил `Government | Majestic 5` влечет за собой наказание!\n> **Настоятельно просим ознакомиться с ними ->** <#1027575999065509898>!')

######################################### MAIN CODE ####################################################################
@bot.tree.command (
    name = 'help',
    description = 'Список доступных команд'
 )  # Слеш команда help
async def help (interaction: discord.Interaction):
    emb = discord.Embed( colour = discord.Color.red(), title = (f'Навигация по командам и возможностям для {interaction.user.name}'))
    emb.add_field (name = '{}start'.format( PREFIX ), value = '\n┗ *Начальная информация для ознакомления*', inline=False)
    emb.add_field (name = '{}close'.format( PREFIX ), value = '\n┗ *Закрыть обращение*. \n ┗`Работает только если вы создали тикет в` <#1038886486700986428>', inline=False)
    emb.add_field (name = '{}state'.format( PREFIX ), value = '\n┗ *Свод актуальных законов Штата*', inline=False)
    emb.add_field (name = '{}yk'.format( PREFIX ), value = '\n┗ *Актуальный УК - Штата*', inline=False)
    emb.add_field (name = '{}leader'.format( PREFIX ), value = '\n┗ *Актуальный список лиц которые занимали пост Губернатора на* `Majestic #5`', inline=False)
    emb.add_field (name = '{}registration'.format( PREFIX ), value = '\n┗ *Регистрация в системе Государственных Закупках* `Majestic #5`', inline=False)

    emb.set_image(url='https://media.discordapp.net/attachments/936659991069331496/1042536977158901881/info_bot.png?width=959&height=350')

    await interaction.response.send_message (embed = emb, ephemeral= True) # ephemeral = True (Приват окно, доступное автору, подробнее смотри - discord.py wiki)


@bot.tree.command(name = 'donate', description = 'Помочь проекту')
async def state (interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}, отлично! Рад что ты решил помочь...\n*Подписка помогает развитию проекта и помогает нам предоставлять обновления в данном направлении...*\n**Воспользуйся сервисом Boosty!** -> https://boosty.to/sub_discordbot", ephemeral= True)

@bot.tree.command(

    name='start',
    description='Информация для ознакомления'
)
async def start(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Привет {interaction.user.mention}! Для продолжения работы просим ознакомиться с командами, используй *slash command* `/help`\nПомни, что **любое** нарушение правил `Government | Majestic 5` влечет за собой наказание!\nНастоятельно просим ознакомиться с ними -> <#1027575999065509898>!",
        ephemeral=True)


@bot.tree.command(
    name='state',
    description='Информация по законам Штата'
)
async def state(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Еще раз привет {interaction.user.mention}! Вижу что освоился, но ты просил уточнить что-то...\nТвой запрос тут -> https://forum.majestic-rp.ru/forums/odobrennye-zakonoproekty.562/",
        ephemeral=True)


@bot.tree.command(
    name='yk', description='Информация по УК'
)
async def state(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"{interaction.user.mention}, отлично! Рад что ты интересуешься...\nТвой запрос тут -> https://forum.majestic-rp.ru/threads/ugolovnyj-kodeks-shtata-sa.466104/",
        ephemeral=True)



lead1 = 'Fester Moss - ID: 4914 - 23.11.2021 - 02.12.2021\n┗[`Был снят по средством Государственного Переворота`]'
lead2 = 'Larry York - ID: 346 - 07.12.2021 - 27.12.2021\n┗[`Был снят Администрацией за слив казны Government`]'
lead3 = 'Yare Fiend - ID: 30470 - 04.01.2022 - 17.02.2022'
lead4 = 'Jesus Valentine - ID: 11296  - 23.02.2022 - 28.03.2022\n┗[`Был снят Администрацией за инактив`]'
lead5 = 'Thomas Ward - ID: 10520 - 03.04.2022 - 03.04.2022\n┗[`Был снят Администрацией за слив информации Администоров`]'
lead6 = 'Archibald Santa - ID: 14210   - 08.04.2022 - 11.05.2022\n┗[`Был снят Администрацией за игру на стороннем проекте`]'
lead7 = 'Zenicu Lena - ID: 45970 - 14.05.2022 - 26.06.2022'
lead8 = 'Insane Paws - ID: 2778 -06.07.2022 - 05.08.2022\n┗[`Был снят Администрацией за получение 3 строгих выговоров`]'
lead9 = 'Yare Fiend - ID: 30470 - 20.08.2022 - 17.09.2022\n┗[`Был снят Администрацией за отсутствие онлайн состава и инактив лидера`]'
lead10 = 'Sergo Lena - ID: 62009 - 02.10.2022 - 16.11.2022'
lead11 = 'Morris Lena - ID: 53685 - 23.11.2022 - по настоящий момент.'

@bot.tree.command(
name = 'leader',
description='Список лидеров Government и их срооки'
)
async def command_leader (interaction: discord.Interaction):
    emb = discord.Embed(colour = discord.Color.purple(),
                        title = (f'Список Губернаторов и их сроков собранные для тебя, {interaction.user.name}'))
    emb.add_field(name = 'Fester Moss', value = lead1, inline=False)
    emb.add_field(name = 'Larry York', value = lead2, inline=False)
    emb.add_field(name = 'Yare Fiend', value = lead3, inline=False)
    emb.add_field(name = 'Jesus Valentine', value = lead4, inline=False)
    emb.add_field(name = 'Thomas Ward', value = lead5, inline=False)
    emb.add_field(name = 'Archibald Santa', value = lead6, inline=False)
    emb.add_field(name = 'Zenicu Lena', value = lead7, inline=False)
    emb.add_field(name = 'Insane Paws', value = lead8, inline=False)
    emb.add_field(name = 'Yare Fiend', value = lead9, inline=False)
    emb.add_field(name = 'Sergo Lena', value = lead10, inline=False)
    emb.add_field(name = 'Morris Lena', value = lead11, inline=False)

    emb.set_image(url='https://media.discordapp.net/attachments/861569518848573440/1047923961306030100/Screenshot_1.png')
    await interaction.response.send_message(embed=emb, ephemeral= True)


# Discord Forms
role = 1027575936981413948 # bind роли для облегчения кода
class MyModal(ui.Modal, title = 'Регистрация в системе закупок'):
    #old_client = ui.TextInput(label = 'Ваше Имя Фамилия, Static_ID',placeholder = 'Пример: Zenicu Lena #45970', style =discord.TextStyle.short)
    new_client = ui.TextInput(label = 'Ваше Имя Фамилия', placeholder='Пример: Zenicu Lena',style = discord.TextStyle.short)
    new_client_id = ui.TextInput(label = 'Ваш статический ID', placeholder='Пример:#45970',style = discord.TextStyle.short)
    buissnes = ui.TextInput(label = 'Ваше предприятие?', placeholder='Пример: Магазин 24/7 № 1 / ИП(название)',style = discord.TextStyle.short)
    about = ui.TextInput(label = 'Имеется судимость?"', placeholder='Пример: Да, по статье (..) / Нет ', style = discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f' <@&{role}> \n\n *Министерству Финансов в лице Министра Финансов Штата San Andreas -* <@292274668977651712>\n *от гражданина* <@{interaction.user.id}>\n\n                 **Заявление**     \n*Я гражданин Штата San Andreas* `{self.new_client}` *с паспортными данными* `{self.new_client_id}` *подаю заявление на регистрацию меня и моего предприятия* `{self.buissnes}`.\n*Так-же настоящим сообщаю что наличие судимости:* `{self.about}`.\n\n *Способ связи:* `email` - <@{interaction.user.id}>.\n*С Уважением* {interaction.user.nick}')

@bot.tree.command(name = 'registration', description = 'Регистрация в системе закупок')
async def modal(interaction: discord.Interaction):
    await interaction.response.send_modal(MyModal())

class MyModal1(ui.Modal, title = 'Кадровый Аудит - Принятие'):
    #old_client = ui.TextInput(label = 'Ваше Имя Фамилия, Static_ID',placeholder = 'Пример: Zenicu Lena #45970', style =discord.TextStyle.short)
    new_client = ui.TextInput(label = 'Имя Фамилия, Static_ID кого приняли', placeholder='Пример: George Lena ',style = discord.TextStyle.short)
    rang = ui.TextInput(label = 'Принят на какой ранг?', placeholder='Пример: 0 - 2',style = discord.TextStyle.short)
    about = ui.TextInput(label = 'Причина принятия?', placeholder='Пример: Набор', style = discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'**Сотрудник:** `{interaction.user.nick}`\n**Гражданин:** `{self.new_client}`\n**Принят на:** `{self.rang}`\n**По причине:** `{self.about}`')

@bot.tree.command(name = 'invite', description = 'Прием сотрудника (Кадровый)')
async def modal(interaction: discord.Interaction):
    await interaction.response.send_modal(MyModal1())

class MyModal11(ui.Modal, title = 'Кадровый Аудит - Повышение/Понижение'):
    #old_client = ui.TextInput(label = 'Ваше Имя Фамилия, Static_ID', placeholder = 'Пример: Zenicu Lena #45970', style =discord.TextStyle.short)
    new_client = ui.TextInput(label = 'Имя Фамилия, Static_ID человека', placeholder='Пример: George Lena #8913 ',style = discord.TextStyle.short)
    rang = ui.TextInput(label = 'Повышен на какой ранг?', placeholder='Пример: 8 - 13',style = discord.TextStyle.short)
    about = ui.TextInput(label = 'Причина повышенеия?', placeholder='Пример: Отчет', style = discord.TextStyle.short)


    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'**Сотрудник:** `{interaction.user.nick}`\n**Повысил/Понизил:** `{self.new_client}`\n**Новый ранг:** `{self.rang}`\n**По причине:** `{self.about}`')

@bot.tree.command(name = 'giverank', description = 'Повыжение/Понижение (Кадровый)')
async def modal1(interaction: discord.Interaction):
    await interaction.response.send_modal(MyModal11())

class MyModal111(ui.Modal, title = 'Кадровый Аудит - Увольнение'):
    #old_client = ui.TextInput(label = 'Ваше Имя Фамилия, Static_ID', placeholder = 'Пример: Zenicu Lena #45970', style =discord.TextStyle.short)
    old_client = ui.TextInput(label = 'Имя Фамилия, Static_ID человека', placeholder='Пример: George Lena #8913 ',style = discord.TextStyle.short)
    aboutt = ui.TextInput(label = 'Причина увольнения?', placeholder='Пример: Не прошел стажировку', style = discord.TextStyle.short)
    black_list = ui.TextInput(label = 'Отметка о ЧС', placeholder=f'Пример: Внесен в ЧС [Не прошел стажировку]', style = discord.TextStyle.short)


    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'**Сотрудник:** `{interaction.user.nick}`\n**Уволил:** `{self.old_client}`\n**Причина увольнения:** `{self.aboutt}`\n**Данные о занесении в ЧС:** `{self.black_list}`')

@bot.tree.command(name = 'uninvite', description = 'Увольнение (Кадровый)')
async def modal1(interaction: discord.Interaction):
    await interaction.response.send_modal(MyModal111())



# import второй части библиотек для работы тикет системы
import discord
from discord import app_commands
from discord.ui import Button, View, Select
from discord.ext import commands
import asyncio
import env






################################################################################################
#  [!]   Тикет система                                                                         #
                                                                                               #
GUILD_ID =  905216984881442817 # Ввести идентификатор сервера (ID)                             #
TEAM_ROLE =  1038883143974932480 # Роль которая должна видеть все входящие обращения           #
TIKECT_CHANNEL = 1038886486700986428 # Канал на котором будут открываться билеты.              #
CATEGORY_ID = 1027651153892212806 # Категория в которой должны быть созданны билеты.           #
################################################################################################

################################################################################################
#   [!]    Система оповещения о новых тикетах.
################################################################################################
MODER_TEXT_ID =  1038881483198320680 # Какнал для информирования Представителей о новом тикете
ROLE_MODER_ID =  1038883143974932480 # ID Role Предстапвителя
#################################################################################################





@bot.command(pass_context = True)
async def ticket(ctx, amount = 1):
    await ctx.channel.purge ( limit = amount )
    button1 = Button(label="📩 Создать обращение", style=discord.ButtonStyle.success, custom_id="ticket_button")
    #button2 = Button(label="⛔️ Закрыть тикет", style=discord.ButtonStyle.danger, custom_id="ticket_button_close")
    view = View()
    view.add_item(button1)
    #view.add_item(button2)
    embed = discord.Embed(description=f"Доброго времени суток!\n\nЕсли у Вас возникли вопросы или Вам необходимо записаться на прием, то воспользуйтесь функцией `Создать обращение`", title=f"Обращения в Правительство")
    embed.set_image(url='')

    channel = bot.get_channel(TIKECT_CHANNEL)
    await channel.send(embed=embed, view=view)
    await ctx.reply("Ожидайте")

@bot.event
async def on_interaction(interaction):
    if interaction.channel.id == TIKECT_CHANNEL:
     if "ticket_button" in str(interaction.data):
       guild = bot.get_guild(GUILD_ID)
       for ticket in guild.channels:
        if str(interaction.user.id) in ticket.name :
            embed = discord.Embed(description=f"Здравствуйте, сейчас вы будете перенаправлены в канал с вашим обращением\nНе выходите с данного канала. {ticket.mention}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

    category = bot.get_channel(CATEGORY_ID)
    ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user.id}",category=category, topic=f"Ticket von {interaction.user} \nClient-ID: {interaction.user.id}")

    await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE), send_messages=True, read_messages=True, add_reactions=False,
                                        embed_links=True, attach_files=True, read_message_history=True,
                                        external_emojis=True)
    await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                        embed_links=True, attach_files=True, read_message_history=True,
                                        external_emojis=True)
    

    embed = discord.Embed(description=f"Приветствую тебя  {interaction.user.mention}! \n\nВ ближайшее время вам ответит `Представитель правительства` для решения вашей проблемы."
                          f"Ожидайте! \n"
                          f"Для закрытия тикеты используйте команду - `/close`",
                color=62719)
 

    embed.set_author(name=f"Новое обращение от {interaction.user.id}")

    #button2 = Button(label="⚠️ Закрыть тикет", style=discord.ButtonStyle.danger, custom_id="ticket_close")
    #view = View()
    #view.add_item(button2)

    category2 = bot.get_channel(MODER_TEXT_ID)
    mess_2 = await ticket_channel.send(embed=embed)
    embed = discord.Embed(title="Обращение создано.",
                         description=f"Ваше обращение будет рассмотрено в -> {ticket_channel.mention}",
                         color=discord.colour.Color.green())
   
    await interaction.response.send_message(embed=embed, ephemeral=True)           

    await category2.send(f'<@&1038883143974932480>\n**Создано обращение! ->** {ticket_channel.mention}\n> Оставь реакцию :white_check_mark: если взяли обращение!')

    return   

#Команда удаления обращения после помощи.
@bot.command(pass_context = True)
async def close(ctx, amount = 1):
    await ctx.channel.purge ( limit = amount )
    button = Button( label = 'Университет Штата', style=discord.ButtonStyle.blurple, emoji = '🎓')
    button2 = Button( label = 'State Fraction #5', style=discord.ButtonStyle.green, emoji = '❤️')
    #Специальная кнопка для фанатов семьи Lena FamQ
    button3 = Button( label = 'Стать фанатом', style=discord.ButtonStyle.blurple, emoji = '🖖🏼')
    
    view = View()
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    if "ticket" in ctx.channel.name:
        embed = discord.Embed(
            description=F"Всего хорошего!",
            color=16711680)
        await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.delete()
        await ctx.author.send ('**Спасибо за обращение!**', view=view)
    async def button_callback(interaction):
        await interaction.response.send_message(content = 'https://discord.gg/MXpP6ccUyj')
    async def button2_callback(interaction):
        await interaction.response.send_message(content = 'https://discord.gg/YmzDXQBaW3')
    async def button3_callback(interaction):
        await interaction.response.send_message(content = 'https://discord.gg/hME7qbDx8H')

    button.callback = button_callback
    button2.callback = button2_callback
    button3.callback = button3_callback







bot.run(env.TOKEN)