import getConfig from 'next/config'
import Endpoints from '@/endpoints'

export async function fetch_registration_options(id: number, username: string) {
  const { publicRuntimeConfig } = getConfig()
  const api_url = publicRuntimeConfig.api_url

  const response = await fetch(
    Endpoints.generateRegistrationOptions(id, username),
  )
  return await response.json()
}
