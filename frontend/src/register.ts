import endpoints from '@/endpoints'
import { startRegistration } from '@simplewebauthn/browser'
import {
  fetch_registration_options,
  verify_registration_options,
} from '@/webauthn'

export async function send_login_code(phone: string) {
  const response = await fetch(endpoints.userLogin(phone))
  if (response.ok) {
    return await response.json()
  } else {
    return null
  }
}

export async function sign_up(
  phone: string,
  phone_hash: string,
  code: string,
  passwd: string,
) {
  const response = await fetch(endpoints.signUp, {
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify({
      phone: phone,
      phone_hash: phone_hash,
      code: code,
      password: passwd,
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  })

  const data = await response.json()

  const registrationOptions = await fetch_registration_options(
    data.user_id,
    data.phone,
  ) // 使用 phone 作为 username 防止无 username 的情况出现

  const registration = await startRegistration(registrationOptions)

  return await verify_registration_options(registration)
}
