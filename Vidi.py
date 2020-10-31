import requests
from bs4 import BeautifulSoup 
import os 
import time 
import urllib.request

from discord.ext import commands
from dotenv import load_dotenv 

load_dotenv('discord_info.env')
TOKEN = os.getenv('DISCORD_TOKEN') 

bot = commands.Bot(command_prefix='-') 

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

@bot.command('news') 
@commands.has_role('root') 
async def news(ctx): 
    
    check_link = '' 
    while True:  
        news = requests.get('https://thehackernews.com/') 
        page = news.content 
    
        info = BeautifulSoup(page, 'lxml') 
        final_info = info.find_all('div', class_= 'body-post clear')
 
        
        if (check_link != final_info[0].a['href']):
            check_link = final_info[0].a['href']
            await ctx.send(check_link) 
        else: 
            await time.sleep(3600) 
  
@bot.command('ctfs')
async def ctf(ctx): 
    ctf_page = requests.get('https://ctftime.org/event/list/?year=2020&online=-1&format=0&restrictions=-1&upcoming=true', headers=headers).content  
   
    
    ctf_info = BeautifulSoup(ctf_page, 'lxml') 
    final_ctf_info = ctf_info.findAll('a')

    #top_five = final_ctf_info[0].a['href']
    
 
    
    #req = urllib.request.Request('https://ctftime.org/event/list/?year=2020&online=-1&format=0&restrictions=-1&upcoming=true', headers=headers) 
    #html_page = urllib.request.urlopen(req)
    #soup = BeautifulSoup(html_page, "lxml") 
    #for link in soup.findAll('a'): 
    #    print(link.get('href')) 


    print(top_five)
    await ctx.send(top_five)
    
    
bot.run(TOKEN) 