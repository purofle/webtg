import React from 'react'
import Link from 'next/link'
import WideButton from '@/components/button'

export default function Home() {
  return (
    <>
      <button></button>
      <Link href="/signup">
        <WideButton>注册</WideButton>
      </Link>
    </>
  )
}
