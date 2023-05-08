import React, { MouseEventHandler } from 'react'

interface ButtonProps {
  children?: any
  onClick?: MouseEventHandler<any> | undefined
}

export default function WideButton(props: ButtonProps) {
  return (
    <button
      className="flex w-full justify-center
        rounded-mdpx-3 py-1.5 text-sm font-semibold
        leading-6 shadow-sm hover:bg-indigo-500
        focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600
        bg-indigo-600"
      onClick={props.onClick}
    >
      {props.children}
    </button>
  )
}
