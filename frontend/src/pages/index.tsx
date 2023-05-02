import {fetch_registration_options} from "@/webauthn";

export default function Home() {
  return (
    <>
      <button onClick={
        async () => {
          console.log(await fetch_registration_options(114514, "nmsl"))
        }
      }>
        <text>start registration</text>
      </button>
    </>
  )
}
