import React, {useState} from "react"
import Image from "next/image"
import NormalInput from "@/components/input"
import logoPic from "@/../public/logo.png"

export default function Home() {
  const [phone, setPhone] = useState("")
  const [code, setCode] = useState("")
  const disabledButton = code.length == 0
  return (
    <>
      <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <Image className="mx-auto h-10 w-auto" src={logoPic}
                 alt="Your Company" width={640} height={640}/>
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">注册</h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form className="space-y-6" action="#" method="POST">
            <div>
              <label htmlFor="email" className="block text-sm font-medium leading-6 text-gray-900">手机号</label>
              <div className="mt-2">
                <NormalInput id="phone" name="phone" type="tel" autoComplete="tel" required={true} onEvent={(event) => {
                  setPhone(event.target.value)
                }}/>
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label htmlFor="number" className="block text-sm font-medium leading-6 text-gray-900">验证码</label>
              </div>
              <div className="mt-2">
                <NormalInput id="number" name="number" type="number" autoComplete="number" required={true} onEvent={(event) => {
                  setCode(event.target.value)
                }}>
                  <button type="button" className="">
                    <label className="block text-sm font-medium leading-6 text-indigo-600">获取验证码</label>
                  </button>
                </NormalInput>

              </div>
            </div>
            <div>
              <button type="submit"
                      className={`flex w-full justify-center rounded-md px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 bg-indigo-600 ${disabledButton ? "text-gray-400" : "text-white"}`}
              >
                注册
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  )
}
