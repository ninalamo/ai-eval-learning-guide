import type { NextConfig } from "next";
import path from "node:path";
import { fileURLToPath } from "node:url";

const webDir = path.dirname(fileURLToPath(import.meta.url));

const nextConfig: NextConfig = {
  // Server loaders read ../curriculum. Do not copy exercises/ into public/
  // (week-04 .env and later API keys must not be statically served).
  outputFileTracingRoot: path.join(webDir, ".."),
};

export default nextConfig;
