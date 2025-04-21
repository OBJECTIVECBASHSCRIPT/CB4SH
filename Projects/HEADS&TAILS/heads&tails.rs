use rand::Rng;
 
//randomly generates heads or tails:
fn main() {
    let mut rng = rand::thread_rng();

    let flip = rng.gen_bool(0.5);


//prints either heads or tails
    match flip {
        true => println!("Heads"),
        false => println!("Tails"),
    }
}
