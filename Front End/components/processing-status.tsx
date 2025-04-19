import { CheckCircle2, Circle, Clock } from "lucide-react"
import { cn } from "@/lib/utils"

type Step = {
  name: string
  status: "pending" | "in-progress" | "complete"
}

interface ProcessingStatusProps {
  steps: Step[]
}

export function ProcessingStatus({ steps }: ProcessingStatusProps) {
  return (
    <div className="space-y-4">
      {steps.map((step, index) => (
        <div key={step.name} className="flex items-center gap-3">
          <div className="flex-shrink-0">
            {step.status === "complete" ? (
              <CheckCircle2 className="h-5 w-5 text-green-500" />
            ) : step.status === "in-progress" ? (
              <Clock className="h-5 w-5 text-amber-500 animate-pulse" />
            ) : (
              <Circle className="h-5 w-5 text-muted-foreground" />
            )}
          </div>

          <div className="flex-grow">
            <div className="flex justify-between items-center">
              <span
                className={cn(
                  "font-medium",
                  step.status === "complete" && "text-green-500",
                  step.status === "in-progress" && "text-amber-500",
                )}
              >
                {step.name}
              </span>
              <span className="text-xs text-muted-foreground">
                {step.status === "complete"
                  ? "Completed"
                  : step.status === "in-progress"
                    ? "In progress..."
                    : "Pending"}
              </span>
            </div>

            {index < steps.length - 1 && <div className={cn("ml-2.5 mt-1 mb-1 w-px h-4 bg-border")} />}
          </div>
        </div>
      ))}
    </div>
  )
}
