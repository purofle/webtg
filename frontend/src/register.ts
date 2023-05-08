import Endpoints from '@/endpoints'

export async function send_login_code(phone: string) {
  const response = await fetch(Endpoints.userLogin(phone))
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
) {}
