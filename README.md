import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We woke up {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('İklim değişikliği nedir'):
        await message.channel.send("İklim sistemi, atmosfer, kara yüzeyleri, kar ve buz, okyanuslar ve diğer su kütleleri ile canlıları kapsayan karmaşık ve etkileşimli bir sistemdir. Bu sistem, zaman içinde, kendi iç dinamiklerinin etkisi altında veya dış etmenlerdeki (zorlamalar olarak adlandırılmaktadır) değişikliklere bağlı olarak yavaş yavaş değişim gösterir. Dış zorlamalar, volkanik patlamalar ve güneşle ilgili değişkenlikler gibi doğal olaylar ile atmosferin bileşimindeki insan kaynaklı değişiklikleri içerir. Güneş radyasyonu, iklim sisteminin güç kaynağıdır. Yerkürenin radyasyon dengesini etkileyen, dolayısıyla iklimi değiştiren üç temel yol bulunmaktadır.Gelen güneş radyasyonundaki değişiklikler (Güneşin kendisindeki ya da Yerkürenin yörüngesindeki değişikliklere bağlı olarak) Güneş radyasyonunun yansıtılan kısmındaki değişiklikler (bu kısım albedo olarak adlandırılmaktadır ve bulut örtüsü, aerosoller denilen küçük parçacıklar ya da arazi örtüsündeki değişikliklere bağlı olarak değişebilmektedir) Yerküreden uzaya geri gönderilen uzun dalgalı radyasyondaki değişiklikler (sera gazı salımlarının atmosferdeki birikimlerine bağlı olarak). Bunların yanı sıra, rüzgarlar ve okyanus akıntılarının, Yerküre yüzeyi üzerindeki ısı dağılımında oynadıkları rol nedeniyle, iklim üzerinde önemli etkileri bulunmaktadır.")
    elif message.content.startswith("mevcut iklim durumu nedir"):
        await message.channel.send("Özellikle sanayi devrimi sonrası özellikle 1750’li yıllardan itibaren, hız kazanan insan faaliyetleri etkisiyle atmosferin kompozisyonu değişmekte, sera gazı emisyonları artmaktadır. En önemli sera gazı olan CO2`nin atmosferdeki birikimi sanayi öncesi dönemde yaklaşık 280 ppm'den (milyonda bir parçacık) Mart 2018’de 407,96 ppm'e yükselmiştir. Sanayi öncesi dönemde yaklaşık 715 ppb (milyarda bir parçacık) olan CH4 birikimi, 2017 yılı sonunda 1859 ppb'e çıkmıştır. Küresel atmosferik N2O birikimi sanayi öncesi dönemde yaklaşık 270 ppb düzeyindeyken 2017 yılında 330 ppb'ye çıkmıştır.")
    elif message.content.startswith('iklime nasıl katkı sağlarız'):
        await message.channel.send("çöplerini belirli çöp kutularına atarsan,mangal yaptıktan sonra söndürürsen,valorantta toxiklik yapmazsan iklime en azından 100%0.0.1 yardım etmiş olursun :)")
    else:
        await.message.channel.send("Bu komut bulunamadı")
