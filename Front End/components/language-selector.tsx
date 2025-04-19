"use client"

import { Check, ChevronsUpDown } from "lucide-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Command, CommandEmpty, CommandGroup, CommandInput, CommandItem, CommandList } from "@/components/ui/command"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { useState } from "react"

const languages = [
  {
    value: "asl",
    label: "American Sign Language (ASL)",
    region: "United States, Canada",
  },
  {
    value: "bsl",
    label: "British Sign Language (BSL)",
    region: "United Kingdom",
  },
  {
    value: "auslan",
    label: "Auslan",
    region: "Australia",
  },
  {
    value: "lsf",
    label: "French Sign Language (LSF)",
    region: "France, French-speaking Switzerland, Belgium",
  },
  {
    value: "dgs",
    label: "German Sign Language (DGS)",
    region: "Germany",
  },
  {
    value: "jsl",
    label: "Japanese Sign Language (JSL)",
    region: "Japan",
  },
]

export function LanguageSelector() {
  const [open, setOpen] = useState(false)
  const [value, setValue] = useState("asl")

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button variant="outline" role="combobox" aria-expanded={open} className="w-full justify-between">
          {value ? languages.find((language) => language.value === value)?.label : "Select language..."}
          <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-full p-0">
        <Command>
          <CommandInput placeholder="Search sign language..." />
          <CommandList>
            <CommandEmpty>No language found.</CommandEmpty>
            <CommandGroup>
              {languages.map((language) => (
                <CommandItem
                  key={language.value}
                  value={language.value}
                  onSelect={(currentValue) => {
                    setValue(currentValue === value ? "" : currentValue)
                    setOpen(false)
                  }}
                >
                  <Check className={cn("mr-2 h-4 w-4", value === language.value ? "opacity-100" : "opacity-0")} />
                  <div className="flex flex-col">
                    <span>{language.label}</span>
                    <span className="text-xs text-muted-foreground">{language.region}</span>
                  </div>
                </CommandItem>
              ))}
            </CommandGroup>
          </CommandList>
        </Command>
      </PopoverContent>
    </Popover>
  )
}
