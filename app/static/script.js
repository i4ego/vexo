let currentPage = 1

function openPage(page = 1) {
    $(`#p${currentPage}`).removeClass("active")
    $(".pages").css("transform", `translateY(-${(page - 1) * 100}%)`);
    $(`#p${page}`).addClass("active")
    currentPage = page
}

function closeUI() {
    window.location.href = "/api/close"
}