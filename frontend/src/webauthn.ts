import Endpoints from '@/endpoints'

export async function fetch_registration_options(id: number, username: string) {
  const response = await fetch(
    Endpoints.generateRegistrationOptions(id, username),
  )
  return await response.json()
}
