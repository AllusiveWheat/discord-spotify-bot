declare global {
  namespace NodeJS {
    interface ProcessEnv {
      SPOTIFY_CLIENT_SECRET: string;
      SPOTIFY_CLIENT_ID: string;
      DISCORD_TOKEN: string;
    }
  }
}

export {};
