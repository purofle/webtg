import {fetch_authentication_options} from "@/user/webauthn";
import {startAuthentication} from "@simplewebauthn/browser";

export async function login() {
  const asseResp = await fetch_authentication_options()
  try {
    await startAuthentication(asseResp)
  } catch (error) {
    console.log(error)
  }
}