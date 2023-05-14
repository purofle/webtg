import getConfig from 'next/config'

const { publicRuntimeConfig } = getConfig()
const api_url = publicRuntimeConfig.api_url

interface Endpoints {
  userLogin(phone: string): string
  generateRegistrationOptions(id: number, username: string): string
  generateAuthenticationOptions: string
  verify_registration: string
  signUp: string
}

const endpoints: Endpoints = {
  userLogin: (phone) => `${api_url}/user/login_code?phone=${phone}`,
  generateRegistrationOptions: (id, username) =>
    `${api_url}/user/generate_registration_options?user_id=${id}&username=${username}`,
  generateAuthenticationOptions: `${api_url}/user/generate_authentication_options`,
  verify_registration: `${api_url}/user/verify_registration`,
  signUp: `${api_url}/user/sign_up`,
}

export default endpoints
