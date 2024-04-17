const texts = [
    {
    text: "Experience the pinnacle of luxury and performance in our premium vehicles.",
    position: "top"
    },
    {
    text: "Turn every drive into an unforgettable journey with our luxurious interiors and unparalleled technology.",
    position: "bottom"
    },
    {
    text: "Elevate your driving experience and make a statement on the road with our elegant and powerful luxury cars.",
    position: "top"
    }
]

$(document).ready(function () {
    let currentImageIndex = 0
    const slider = $("#slider-container")
    let interval = null

    function changeTextAndLegendPosition(legendConfig) {
        const legend = $("#legend span")

        legend.text(legendConfig.text)

        const position = legendConfig.position !== "top" ? "calc(100% - 180px)" : "80px"

        $("#legend").css({
          "top": position,
        })
    }

    $("#back").click(() => {
        if (currentImageIndex === 0) {
          currentImageIndex = texts.length - 1
        } else {
          currentImageIndex--
        }

        changeTextAndLegendPosition(texts[currentImageIndex])

        slider.animate({
            scrollLeft: currentImageIndex * slider.width()
        }, 500);
    })

    $("#next").click(() => {
        if (currentImageIndex >= (texts.length - 1)) {
          currentImageIndex = 0
        } else {
          currentImageIndex++
        }

        changeTextAndLegendPosition(texts[currentImageIndex])

        slider.animate({
            scrollLeft: currentImageIndex * slider.width()
        }, 500);
    })

    interval = setInterval(() => {
        if (currentImageIndex >= (texts.length - 1)) {
          currentImageIndex = 0
        } else {
          currentImageIndex++
        }

        changeTextAndLegendPosition(texts[currentImageIndex])
        slider.animate({
            scrollLeft: currentImageIndex * slider.width()
        }, 500);
    }, 5_000)

    $(window).on("beforeunload", function () {
        clearInterval(interval)
    })
})