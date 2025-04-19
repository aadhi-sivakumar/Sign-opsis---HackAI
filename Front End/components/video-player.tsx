"use client"

import { useState, useRef } from "react"
import { Play, Pause, Volume2, VolumeX, Maximize, Subtitles } from "lucide-react"
import { Slider } from "@/components/ui/slider"
import { Toggle } from "@/components/ui/toggle"
import { cn } from "@/lib/utils"

export function VideoPlayer() {
  const [isPlaying, setIsPlaying] = useState(false)
  const [isMuted, setIsMuted] = useState(false)
  const [showSubtitles, setShowSubtitles] = useState(true)
  const [progress, setProgress] = useState(0)
  const [volume, setVolume] = useState(80)
  const [showControls, setShowControls] = useState(true)

  // In a real implementation, this would be a video element ref
  const videoRef = useRef<HTMLDivElement>(null)

  const togglePlay = () => {
    setIsPlaying(!isPlaying)
  }

  const toggleMute = () => {
    setIsMuted(!isMuted)
  }

  const toggleSubtitles = () => {
    setShowSubtitles(!showSubtitles)
  }

  const handleVolumeChange = (value: number[]) => {
    setVolume(value[0])
    if (value[0] === 0) {
      setIsMuted(true)
    } else if (isMuted) {
      setIsMuted(false)
    }
  }

  const handleProgressChange = (value: number[]) => {
    setProgress(value[0])
  }

  return (
    <div
      className="relative rounded-md overflow-hidden bg-black aspect-video"
      onMouseEnter={() => setShowControls(true)}
      onMouseLeave={() => setShowControls(false)}
      ref={videoRef}
    >
      {/* Video placeholder */}
      <div className="absolute inset-0 flex items-center justify-center">
        <div className="w-full h-full bg-gradient-to-br from-purple-900/20 to-pink-900/20 flex items-center justify-center">
          {/* Sign language avatar would be here */}
          <div className="relative w-32 h-32 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
            <span className="text-4xl">👋</span>
          </div>
        </div>
      </div>

      {/* Subtitles */}
      {showSubtitles && (
        <div className="absolute bottom-16 left-0 right-0 text-center">
          <div className="inline-block bg-black/70 text-white px-4 py-2 rounded-md text-sm">
            Hello, welcome to our company update.
          </div>
        </div>
      )}

      {/* Controls overlay */}
      <div
        className={cn(
          "absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-4 transition-opacity duration-300",
          showControls ? "opacity-100" : "opacity-0",
        )}
      >
        {/* Progress bar */}
        <Slider value={[progress]} min={0} max={100} step={1} onValueChange={handleProgressChange} className="mb-4" />

        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <button onClick={togglePlay} className="text-white hover:text-primary transition-colors">
              {isPlaying ? <Pause size={20} /> : <Play size={20} />}
            </button>

            <div className="flex items-center gap-2 ml-2">
              <button onClick={toggleMute} className="text-white hover:text-primary transition-colors">
                {isMuted ? <VolumeX size={20} /> : <Volume2 size={20} />}
              </button>
              <Slider
                value={[isMuted ? 0 : volume]}
                min={0}
                max={100}
                step={1}
                onValueChange={handleVolumeChange}
                className="w-20"
              />
            </div>

            <div className="text-white text-xs ml-2">0:45 / 2:30</div>
          </div>

          <div className="flex items-center gap-2">
            <Toggle
              pressed={showSubtitles}
              onPressedChange={toggleSubtitles}
              size="sm"
              className="text-white data-[state=on]:bg-primary/50"
            >
              <Subtitles size={16} />
            </Toggle>

            <button className="text-white hover:text-primary transition-colors">
              <Maximize size={16} />
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
