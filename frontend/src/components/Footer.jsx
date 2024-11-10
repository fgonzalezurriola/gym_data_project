import { FaGithub } from 'react-icons/fa';

const Footer = () => {
  return (
    <section className="text-black py-4">
      <div className="flex items-center justify-center mx-auto px-4 text-center space-y-4">
        <p className='mx-6 justify-start'>2024 fgonzalezurriola</p>
        <a
          href=""
          target="_blank"
          rel="noreferrer noopener"
          className="text-black dark:text-gray-800 hover:text-customPurple transition duration-300 flex flex-col items-center"
        >
          <FaGithub className="text-3xl" />
            <p className="text-center text-2xl font-bold">Código</p>
        </a>
      </div>
    </section>
  );
};

export default Footer;
