"use client";
import { ImageGallery } from "react-image-grid-gallery";
import styles from "../page.module.css";

const imagesArray = [
  {
    alt: "Image1's alt text",
    caption: "Image1's description",
    src: "https://c2.staticflickr.com/9/8817/28973449265_07e3aa5d2e_b.jpg",
  },
  {
    alt: "Image2's alt text",
    caption: "Image2's description",
    src: "https://c2.staticflickr.com/9/8356/28897120681_3b2c0f43e0_b.jpg",
  },
  {
    alt: "Image3's alt text",
    caption: "Image3's description",
    src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
  },
  {
    alt: "Image3's alt text",
    caption: "Image3's description",
    src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
  },
  {
    alt: "Image3's alt text",
    caption: "Image3's description",
    src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
  },
  {
    alt: "Image3's alt text",
    caption: "Image3's description",
    src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
  },
  {
    alt: "Image3's alt text",
    caption: "Image3's description",
    src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
  },
  {
    alt: "Image3's alt text",
    caption: "Image3's description",
    src: "https://c4.staticflickr.com/9/8887/28897124891_98c4fdd82b_b.jpg",
  },
];

export default function Demo() {
  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <ImageGallery imagesInfoArray={imagesArray} columnWidth={230} />
      </div>
    </main>
  );
}
