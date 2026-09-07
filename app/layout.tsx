import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'EstateFlow — Community Operations',
  description: 'A beautiful estate management and community finance prototype.',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}