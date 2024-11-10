/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        customPurple: '#8884d8',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}