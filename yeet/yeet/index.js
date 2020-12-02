const Discord = require('discord.js');
const bot = new Discord.Client();
const TOKEN = "NTM2NzUyMzM1ODM4NTExMTQ0.DybSNA.NALsCyg32RSFrJLT2HbLQprMnR8"

bot.on('message', function(message){
    if(message.content == "Yeetus that fetus")
    {
        message.reply("No, yeetus MY fetus!");
    }
});

bot.on('ready', function(){
    console.log("Ready");
});

bot.login(TOKEN);