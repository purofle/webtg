/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  publicRuntimeConfig: {
    api_url: 'http://localhost:8000',
  },
}

module.exports = nextConfig
