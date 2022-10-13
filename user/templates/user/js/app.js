const burger = document.querySelector(".burger"),
	nav = document.querySelector(".nav-links"),
	lines = burger.children,
	lists = nav.children,
	closeN = () => {
		for (i = 0; i < lists.length; i++) lists[i].style.display = "none";
		nav.style.width = "0";
	},
	showN = () => {
		(nav.style.width = "100vw"),
			(c = nav.children),
			(window.onclick = function (e) {
				e.target == nav &&
					((lines[0].style.transform = "rotate(0deg)"),
					(lines[0].style.margin = "5px"),
					(lines[1].style.display = "block"),
					(lines[2].style.transform = "rotate(0deg)"),
					(lines[2].style.margin = "5px"),
					(state = !0),
					closeN());
			});
	};
window.innerWidth <= 768 && closeN(),
	window.addEventListener("resize", () => {
		if (window.innerWidth <= 768) {
			for (
				lines[0].style.transform = "rotate(0deg)",
					lines[0].style.margin = "5px",
					lines[1].style.display = "block",
					lines[2].style.transform = "rotate(0deg)",
					lines[2].style.margin = "5px",
					i = 0;
				i < lists.length;
				i++
			)
				lists[i].style.display = "none";
			(state = !0), closeN();
		}
		if (window.innerWidth > 768)
			for (nav.style.width = "60%", i = 0; i < lists.length; i++)
				(lists[i].style.display = "inline"),
					(lists[i].style.float = "left");
	});
let state = !0;
burger.addEventListener("click", () => {
	console.log('clicked');
	if (0 == (state = 1 != state))
		for (
			c = nav.children,
				nav.style.width = "100vw",
				c = nav.children,
				window.onclick = function (e) {
					e.target == nav &&
						((lines[0].style.transform = "rotate(0deg)"),
						(lines[0].style.margin = "5px"),
						(lines[1].style.display = "block"),
						(lines[2].style.transform = "rotate(0deg)"),
						(lines[2].style.margin = "5px"),
						(state = !0),
						closeN());
				},
				lines[0].style.transform = "rotate(45deg)",
				lines[0].style.margin = "-2px",
				lines[1].style.display = "none",
				lines[2].style.transform = "rotate(-45deg)",
				lines[2].style.margin = "-2px",
				i = 0;
			i < c.length;
			i++
		)
			(c[i].style.transition = "0.6s"), (c[i].style.display = "block");
	else
		closeN(),
			(lines[0].style.transform = "rotate(0deg)"),
			(lines[0].style.margin = "05px"),
			(lines[1].style.display = "block"),
			(lines[2].style.transform = "rotate(0deg)"),
			(lines[2].style.margin = "5px");
});
// console.log(lists.classList);
// lists.forEach(list, () => {
// });
