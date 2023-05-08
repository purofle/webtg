import React from 'react'

interface InputProps {
  id: string
  name: string
  type: string
  autoComplete: string
  required: boolean
  onEvent?: { (event: React.ChangeEvent<HTMLInputElement>): void }
  children?: JSX.Element
}

export default function NormalInput(props: InputProps) {
  return (
    <div className="relative">
      <input
        id={props.id}
        name={props.name}
        type={props.type}
        autoComplete={props.autoComplete}
        required={props.required}
        onChange={props.onEvent}
        className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm
                ring-1 ring-inset ring-gray-300 placeholder:text-gray-400
                focus:ring-2 focus:ring-inset focus:ring-indigo-600
                sm:text-sm sm:leading-6
                [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none"
      ></input>
      <div className="absolute inset-y-0 right-0 pr-3 flex items-center">
        {props.children}
      </div>
    </div>
  )
}
