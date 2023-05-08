import React, { useState } from 'react'
import Image from 'next/image'
import NormalInput from '@/components/input'
import logoPic from '@/../public/logo.png'
import { send_login_code } from '@/register'
import { parsePhoneNumber } from 'awesome-phonenumber'
import WideButton from '@/components/button'
import { fetch_registration_options } from '@/webauthn'

export default function SignUp() {
  const [phone, setPhone] = useState('')
  const [code, setCode] = useState('')
  const disabledButton = code.length == 0
  const [waitingCode, setWaitingCode] = useState(true)
  return (
    <>
      <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <Image
            className="mx-auto h-10 w-auto"
            src={logoPic}
            alt="Your Company"
            width={640}
            height={640}
          />
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
            注册
          </h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <div className="space-y-6">
            <div>
              <label
                htmlFor="email"
                className="block text-sm font-medium leading-6 text-gray-900"
              >
                手机号
              </label>
              <div className="mt-2">
                <NormalInput
                  id="phone"
                  name="phone"
                  type="tel"
                  autoComplete="tel"
                  required={true}
                  onEvent={(event) => {
                    setPhone(event.target.value)

                    const pn = parsePhoneNumber(event.target.value)

                    if (pn.valid) {
                      setWaitingCode(false)
                    } else {
                      setWaitingCode(true)
                    }
                  }}
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label
                  htmlFor="number"
                  className="block text-sm font-medium leading-6 text-gray-900"
                >
                  验证码
                </label>
              </div>
              <div className="mt-2">
                <NormalInput
                  id="number"
                  name="number"
                  type="number"
                  autoComplete="number"
                  required={true}
                  onEvent={(event) => {
                    setCode(event.target.value)
                  }}
                >
                  <button
                    type="button"
                    disabled={waitingCode}
                    onClick={async () => {
                      await send_login_code(phone)
                      setWaitingCode(true)
                    }}
                  >
                    <label
                      className={`block text-sm font-medium leading-6 ${
                        waitingCode ? 'text-gray-300' : 'text-indigo-600'
                      }`}
                    >
                      获取验证码
                    </label>
                  </button>
                </NormalInput>
              </div>
            </div>
            <div>
              <WideButton onClick={async () => {}}>
                <label
                  className={`${
                    disabledButton ? 'text-gray-400' : 'text-white'
                  }`}
                >
                  注册
                </label>
              </WideButton>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}
