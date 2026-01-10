/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.{html,js}",
    "../main/templates/**/*.{html,js}",
    "../**/templates/**/*.{html,js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    daisyui: {
  themes: ["lofi", "night", "cyberpunk"],
},

  },
};
