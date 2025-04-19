import type { ReactNode } from "react"
import { Card, CardContent, CardHeader } from "@/components/ui/card"

interface FeatureCardProps {
  icon: ReactNode
  title: string
  description: string
}

const FeatureCard = ({ icon, title, description }: FeatureCardProps) => {
  return (
    <Card className="border-none shadow-sm hover:shadow-md transition-shadow duration-300 bg-white/80 backdrop-blur-sm">
      <CardHeader className="pb-2">
        <div className="rounded-full w-14 h-14 flex items-center justify-center bg-cyan-100 mb-4">{icon}</div>
        <h3 className="text-xl font-semibold">{title}</h3>
      </CardHeader>
      <CardContent>
        <p className="text-muted-foreground">{description}</p>
      </CardContent>
    </Card>
  )
}

export default FeatureCard
