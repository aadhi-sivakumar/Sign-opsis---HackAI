"use client"
import { Canvas } from "@react-three/fiber"
import { Environment, PresentationControls } from "@react-three/drei"
import Image from "next/image"

export default function HeroAnimation() {
  return (
    <div className="relative w-full h-full flex items-center justify-center">
      {/* Display the ASL alphabet image directly using Next.js Image component */}
      <div className="relative w-full h-full flex items-center justify-center">
        <Image
          src="/images/asl-alphabet.jpeg"
          alt="American Sign Language Alphabet"
          fill
          style={{ objectFit: "contain" }}
          priority
        />

        {/* Add the logo as an overlay */}
        <div className="absolute top-4 right-4">
          <Image
            src="/images/sign-language-logo.png"
            alt="Sign Language Logo"
            width={80}
            height={80}
            className="animate-pulse"
          />
        </div>
      </div>

      {/* Keep a simplified 3D background for visual interest */}
      <div className="absolute inset-0 -z-10">
        <Canvas shadows camera={{ position: [0, 0, 5], fov: 50 }}>
          <ambientLight intensity={0.8} />
          <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} castShadow />
          <PresentationControls
            global
            config={{ mass: 2, tension: 500 }}
            snap={{ mass: 4, tension: 1500 }}
            rotation={[0, 0, 0]}
            polar={[-Math.PI / 3, Math.PI / 3]}
            azimuth={[-Math.PI / 1.4, Math.PI / 2]}
          >
            <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -1.5, 0]} receiveShadow>
              <planeGeometry args={[10, 10]} />
              <meshStandardMaterial color="#e6f7f7" />
            </mesh>
          </PresentationControls>
          <Environment preset="city" />
        </Canvas>
      </div>
    </div>
  )
}
