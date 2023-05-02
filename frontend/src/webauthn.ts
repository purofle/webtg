import getConfig from 'next/config'

export async function fetch_registration_options(id: Number, username: string) {

  const { publicRuntimeConfig } = getConfig()
  const api_url = publicRuntimeConfig.api_url

  const response = await fetch(`${api_url}/generate-registration-options?user_id=${id}&username=${username}`)
  return await response.json()
}