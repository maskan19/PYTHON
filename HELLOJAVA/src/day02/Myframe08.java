package day02;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class Myframe08 extends JFrame {

	private JPanel contentPane;
	private JTextField tfCom;
	private JTextField tfMine;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Myframe08 frame = new Myframe08();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Myframe08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lblCom = new JLabel("\uCEF4: ");
		lblCom.setBounds(35, 28, 57, 15);
		contentPane.add(lblCom);

		JLabel lblMine = new JLabel("\uB098:");
		lblMine.setBounds(35, 66, 57, 15);
		contentPane.add(lblMine);

		tfCom = new JTextField();
		tfCom.setBounds(92, 25, 116, 21);
		contentPane.add(tfCom);
		tfCom.setColumns(10);

		tfMine = new JTextField();
		tfMine.setBounds(92, 63, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);

		JLabel lblResult = new JLabel("\uACB0\uACFC:");
		lblResult.setBounds(35, 109, 57, 15);
		contentPane.add(lblResult);

		tfResult = new JTextField();
		tfResult.setBounds(92, 106, 116, 21);
		contentPane.add(tfResult);
		tfResult.setColumns(10);

		JButton btn = new JButton("\uC2E4\uD589\uD558\uAE30");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int com = (int) (Math.random() * 3);
				int mine = tfMine.getText().equals("????") ? 0 : tfMine.getText().equals("????") ? 1 : 2;
				String s_com = com == 0 ? "????" : com == 1 ? "????" : "??";
				String result = mine - com == 1 || mine - com == -2 ? result = "?¸?" : mine == com ? "???º?" : "?й?";
				tfCom.setText(s_com);
				tfResult.setText(result);
			}
		});
		btn.setBounds(35, 163, 97, 23);
		contentPane.add(btn);
	}

}
