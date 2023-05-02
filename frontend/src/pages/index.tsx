import React, {useState} from "react";
import Image from "next/image";
import NormalInput from "@/components/input";

export default function Home() {
  const [phone, setPhone] = useState("")

  return (
    <>
      <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <Image className="mx-auto h-10 w-auto" src=""
               alt="Your Company" width={200} height={200} />
            <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">注册</h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form className="space-y-6" action="#" method="POST">
            <div>
              <label htmlFor="email" className="block text-sm font-medium leading-6 text-gray-900">Email address</label>
              <div className="mt-2">
                <NormalInput id="phone" name="phone" type="tel" autoComplete="tel" required={true} />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label htmlFor="password" className="block text-sm font-medium leading-6 text-gray-900">Password</label>
                <div className="text-sm">
                  <a href="#" className="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
                </div>
              </div>
              <div className="mt-2">
                <NormalInput id="password" name="password" type="password" autoComplete="current-password" required={true} />
              </div>
            </div>

            <div>
              <button type="submit"
                      className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign
                in
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  )
}
