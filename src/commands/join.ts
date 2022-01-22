import { SlashCommandBuilder } from "@discordjs/builders";

module.exports = {
  data: new SlashCommandBuilder()
    .setName("join")
    .setDescription("Joins the voice channel!"),
  async execute(interaction) {
    await interaction.reply("Joining voice channel!");
    await interaction.guild.channels.cache
      .find((channel) => channel.name === "general")
      .join();
  },
};
