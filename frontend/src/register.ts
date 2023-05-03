import getConfig from "next/config";

export async function send_login_code(phone: string) {

  const { publicRuntimeConfig } = getConfig()
  const api_url = publicRuntimeConfig.api_url

  const response = await fetch(`${api_url}/user/login_code?phone=${phone}`)
  if (response.ok) {
    return await response.json()
  } else {
    return null
  }
}