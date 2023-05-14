import Image from 'next/image'
import logoPic from '../../public/logo.png'
import React from 'react'
import WideButton from '@/components/button'
import {login} from "@/user/login";

export default function SignIn() {
  return (
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
          登录
        </h2>
      </div>

      <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <div className="space-y-6">
          <WideButton onClick={
            async () => {
              await login()
            }
          }>使用 WebAuthn 登录</WideButton>
        </div>
      </div>
    </div>
  )
}
