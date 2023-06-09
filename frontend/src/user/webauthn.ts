import endpoints from '@/api/endpoints'
// @ts-ignore
import {RegistrationResponseJSON} from '@simplewebauthn/typescript-types'

export async function fetch_registration_options(id: number, username: string) {
  const response = await fetch(
    endpoints.generateRegistrationOptions(id, username),
  )
  return await response.json()
}

export async function fetch_authentication_options() {
  const response = await fetch(
    endpoints.generateAuthenticationOptions,
  )
  return await response.json()
}

export async function verify_registration_options(
  registration_response: RegistrationResponseJSON,
  token: string,
) {
  const response = await fetch(endpoints.verify_registration, {
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify(registration_response),
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
  })
}
