import Breadcrumb from "@/components/Common/Breadcrumb";
import Contact from "@/components/Contact";

import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact us",
  description: "This is Contact us page",
};

const ContactPage = () => {
  return (
    <>
      <Breadcrumb
        pageName="Contact us"
        description=""
      />

      <Contact />
    </>
  );
};

export default ContactPage;
