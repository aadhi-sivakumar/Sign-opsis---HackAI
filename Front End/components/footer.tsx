import Link from "next/link"
import Image from "next/image"

const Footer = () => {
  return (
    <footer className="border-t bg-background">
      <div className="container py-8 md:py-12">
        <div className="flex flex-col items-center text-center">
          <Link href="/" className="flex items-center gap-2">
            <Image
              src="/images/sign-language-logo.png"
              alt="Sign-opsis Logo"
              width={32}
              height={32}
              className="rounded-full"
            />
            <span className="font-bold text-lg">Sign-opsis</span>
          </Link>
          <p className="mt-4 text-sm text-muted-foreground max-w-md">
            Sign-opsis converts audio content into sign language videos, making media accessible to the deaf and hard of
            hearing community.
          </p>
        </div>
        <div className="mt-8 pt-8 border-t text-center text-sm text-muted-foreground">
          <p>© {new Date().getFullYear()} Sign-opsis. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}

export default Footer
