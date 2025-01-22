import ScrollUp from "@/components/Common/ScrollUp";
import Contact from "@/components/Contact";
import Features from "@/components/Features";
import Hero from "@/components/Hero";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "AgriNet", 
};

export default function Home() {
  return (
    <>
      <ScrollUp />
      <Hero />
      <Features />
      <Contact />
    </>
  );
}
