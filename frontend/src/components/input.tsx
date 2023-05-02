import React from "react";

interface InputProps {
  id: string
  name: string
  type: string
  autoComplete: string
  required: boolean
}

export default function NormalInput(props: InputProps) {
  return <input id={props.id} name={props.name} type={props.type} autoComplete={props.autoComplete} required={props.required}
                       className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
}