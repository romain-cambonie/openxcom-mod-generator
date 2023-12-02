(define (script-fu-indexed input-image output-image palette-name num-cols)
  (let* ((image (car (gimp-file-load RUN-NONINTERACTIVE input-image input-image)))
         (drawable (car (gimp-image-flatten image))))
    
    (gimp-image-convert-indexed image NO-DITHER CUSTOM-PALETTE num-cols FALSE FALSE palette-name)
    (file-png-save RUN-NONINTERACTIVE image drawable output-image output-image FALSE 9 FALSE FALSE FALSE FALSE FALSE)
    
    (gimp-image-delete image)
  )
)

(script-fu-register "script-fu-indexed"
                    "Convert to Indexed with Custom Palette"
                    "Converts an RGB image to indexed mode using a specified palette."
                    "Your Name" "Your Name" "2023"
                    "*"
                    SF-STRING "Input image" ""
                    SF-STRING "Output image" ""
                    SF-STRING "Palette name" ""
                    SF-VALUE "Number of colors" "256"
)

(script-fu-menu-register "script-fu-indexed"
                         "<Image>/File")

