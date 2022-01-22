const { SlashCommandBuilder } = require("@discordjs/builders");
const { REST } = require("@discordjs/rest");
const { Routes } = require("discord-api-types/v9");
const dotenv = require("dotenv-safe");
const fs = require("fs");
dotenv.config({ allowEmptyValues: true });
const clientId = process.env.DISCORD_CLIENT_ID;
const token = process.env.DISCORD_TOKEN;
const guildId = process.env.DISCORD_GUILD_ID;
const commands: any = [];
const commandFiles = fs
  .readdirSync("./commands")
  .filter((file) => file.endsWith(".js"));

for (const file of commandFiles) {
  const command = require(`./commands/${file}`);
  commands.push(command.data.toJSON());
}
const rest = new REST({ version: "9" }).setToken(token);

rest
  .put(Routes.applicationGuildCommands(clientId, guildId), { body: commands })
  .then(() => console.log("Successfully registered application commands."))
  .catch(console.error);
