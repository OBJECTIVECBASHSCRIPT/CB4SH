use monero::{PrivateKey, PublicKey, Address};
use rand::rngs::OsRng;

fn main() {
   // TODO: Write Monnero automation logic here
   let spend_key = PrivateKey::generate(&mut OsRng);
   let view_key = PrivateKey::generate(&mut OsRng);

   let spend_pub = PublicKey::from_private_key(&spend_key);
   let view_pub = PublicKey::from_private_key(&view_key);

   let address = Address::standard(Network::Mainnet, &spend_pub, &view_pub);

     println!("Spend Key: {:?}", spend_key);
     println!("View Key {:?}", view_key);
     println("Address: {}", address);
     println!("ready to shuffle!");
}
  



