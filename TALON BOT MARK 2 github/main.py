import discord
from discord.ext import commands
from discord import Interaction


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} está logado!")
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, status=discord.Status.do_not_disturb, name="Not Even Ghosts Are This Empty - $uicideboy$"))



@bot.command(
        aliases = ['spike', 'powerspike', 'powerspikes'], 
        help = "Use para ver os picos de poder do talon!",
        description = "Veja quais os melhores momentos do talon durante o jogo!"
)


async def spikes(ctx):
    await ctx.send("**PRIMEIRO SPIKE:** Punhal Serrilhado + 2 long swords / Chicote Ferrifarpo. Motivo -> Clear Wave nvl 7!\n**SEGUNDO SPIKE:** Mítico fechado (este é o primeiro spike do talon jungle)\n**TERCEIRO SPIKE:** Garra / Cutelo. Motivo -> Muito dano e muito cdr\n**OUTROS SPIKES:** Axioma / Serylda / Chuva de Canivete. Motivo -> Mais penetração, cdr e burst!")




@bot.command(
        aliases = ['playlist'],
        help = "Use para ter a playlist de hardstyle",
        description = "Playlist de hardstyle de kdoizz talon"
)

async def hardstyle(ctx):
    await ctx.send("https://www.youtube.com/playlist?list=PLZxqilbYAz_dsUYtA1eIof8Af8OD6BGWL")


@bot.command(
        aliases = ['build'],
        help = "Use para ver as melhores runas e builds atualmente do talon mid/jungle!",
        description = "Veja quais as melhores runas e builds do talon mid/jungle!"
)


async def runas(ctx):
    img_url = 'https://i.imgur.com/TTeniSB.png'
    embed = discord.Embed()
    embed.set_image(url=img_url)
    await ctx.send("\n**CONQUEROR MID:** Complete a build com itens como Shojin, Malmortius, >> NÃO << FAÇA DEATH DANCE, OU ITENS DE LETHALITY!!\n**FIRST STRIKE:** Complete a build com SERYLDA->CUTELO normalmente, caso não tenha muito armadura termine com canivetes no lugar do cutelo!\n**CONQUEROR JG:** Não gosto de eclipse, termino normalmente com AXIOMA->SHOJIN\n", embed=embed)


@bot.command(
        aliases = ['wr'],
        help = "Após o comando coloque seu número de vitórias, seu número de derrotas e o winrate desejado (sem %)",
        description = "Calcule seu winrate! Descubra quantas vitórias falta pro seu winrate desejado!"
)


async def winrate(ctx, vitorias: int, derrotas: int, winrate_desejado: int):
    total_jogos = vitorias + derrotas
    winrate_atual = (vitorias / total_jogos) * 100
    await ctx.send(f'O winrate do jogador é: {winrate_atual:.2f}%')

    if winrate_desejado <= winrate_atual:
        await ctx.send("Você já atingiu ou ultrapassou o winrate desejado!")
    else:
        vit_necessarias = 0
        while winrate_atual < winrate_desejado:
            vitorias += 1
            vit_necessarias += 1
            winrate_atual = (vitorias / (vitorias + derrotas)) * 100
        await ctx.send("Vitórias necessárias para atingir {:.2f}% de winrate: {}".format(winrate_desejado, vit_necessarias))


@winrate.error
async def winrate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Digite, respectivamente, o número de vitórias, derrotas e seu winrate desejado (sem %)!")


@bot.tree.command(name="ping", description="Mostrará a latência do Talon Bot!")
async def ping(interaction : Interaction):
    bot_latency = round(bot.latency*1000)
    await interaction.response.send_message(f"Pong! {bot_latency}ms")


@bot.tree.command()
async def otp(interaction : Interaction):
    embed = discord.Embed(title="TALON OTP STREAMERS", color=0xff0000)

    table_data = [
        ("Player", "[EUW] LurkZ77", "[BR] Guilty", "[EUW] KaosAngel"),
        ("Stream", "tw.tv/lurkz77", "tw.tv/guilty", "tw.tv/kaos_angel"),
        ("Youtube", "yt.com/@LurkZ77", "yt.com/@GuiltyTalonStream", "yt.com/@KaostanzaLoL"),
    ]

    for row in table_data:
        embed.add_field(name=row[0], value=f"{row[1]}\n{row[2]}\n{row[3]}", inline=True)

    await interaction.response.send_message(embed=embed)


bot.run("SECRET TOKEN :3")