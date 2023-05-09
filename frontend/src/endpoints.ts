import getConfig from 'next/config'

const { publicRuntimeConfig } = getConfig()
const api_url = publicRuntimeConfig.api_url

interface Endpoints {
  userLogin(phone: string): string
  generateRegistrationOptions(id: number, username: string): string
  signUp: string
}

const endpoints: Endpoints = {
  userLogin: (phone) => `${api_url}/user/login_code?phone=${phone}`,
  generateRegistrationOptions: (id, username) =>
    `${api_url}/user/generate-registration-options?user_id=${id}&username=${username}`,
  signUp: `${api_url}/user/sign_up`,
}

export default endpoints
