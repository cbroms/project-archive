import posts from './_posts.js';

const contents = JSON.stringify(posts.map(post => {

  let image = post.image !== undefined ? post.image.split(".") : ["default", "jpg"]
  let smallImage =  image[0] + "-thumb.jpg"
  let mediumImage = image[0] + "-mid.jpg"

  if (image[1] === "gif") {
    smallImage = image[0] + "-gif-mid.jpg"
    mediumImage = image[0] + "-mid.gif"
  }

  return {
    title: post.title,
    slug: post.slug,
    smallImage: smallImage,
    mediumImage: mediumImage,
    category: post.category,
    printDate: post.printDate,
  };
}));

export function get(req, res) {
  res.writeHead(200, {
    'Content-Type': 'application/json'
  });

  res.end(contents);
}
